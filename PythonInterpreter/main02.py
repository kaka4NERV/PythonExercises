import dis,sys


class VirtualMachineError(Exception):
    pass

class VirtualMachine(object):
    def __init__(self):
        self.frames = []  # 调用栈
        self.frame = None  # 当前帧
        self.return_value = None
        self.last_exception = None

    def run_code(self, code, global_names=None, local_names=None):
        # 使用VirtualMachine实行代码的入口
        frame = self.make_frame(code, global_names=global_names,
                                local_names=local_names)
        self.run_frame(frame)

    # 操作帧
    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        if global_names is not None and local_names is not None:
            local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = {}
        else:
            global_names = local_names ={
                '__builtins__': __builtins__,
                '__names__': '__main__',
                '__doc__': None,
                '__package__': None,
            }
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame

    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None

    def run_frame(self):
        pass

    # 数据栈的操作
    def top(self):
        return self.frame.stack[-1]

    def pop(self):
        return self.frame.stack.pop()

    def push(self, *vals):
        self.frame.stack.extend(vals)

    def popn(self, n):
        '''从数据栈中弹出许多的值，返回一个‘n’值的列表，最深的值在最前面'''
        if n:
            ret = self.frame.stack[-n:]
            self.frame.stack[-n:] = []
            return ret
        else:
            return []

    def parse_byte_and_args(self):
        f = self.frame
        opoffset = f.last_instruction
        byteCode = f.code_obj.co_code[opoffset]
        f.last_instruction += 1
        byte_name = dis.opname[byteCode]  # dis.opname-->Sequence of operation names, indexable using the bytecode.
        if byteCode >= dis.HAVE_ARGUMENT:  # don’t take arguments < HAVE_ARGUMENT and those which do >= HAVE_ARGUMENT.
            # index intothe bytecode
            arg = f.code_obj.co_code[f.last_instruction:f.last_instruction+2]
            f.last_instruction += 2  # 下移读取指令的指针
            arg_val = arg[0] + (arg[1] * 256)
            if byteCode in dis.hasconst:  # 查找常量
                arg = f.code_obj.co_consts[arg_val]
            elif byteCode in dis.hasname:  # 查找变量
                arg = f.code_obj.co_names[arg_val]
            elif byteCode in dis.haslocal:  # 查找本地变量
                arg = f.code_obj.co_varnames[arg_val]
            elif byteCode in dis.hasjrel:  # 计算关联跳转
                arg = f.last_instruction + arg_val
            else:
                arg = arg_val
            argument = [arg]
        else:
            argument = []

        return byte_name, argument

    def dispatch(self, byte_name, argument):
        """ Dispatch by bytename to the corresponding methods.
               Exceptions are caught and set on the virtual machine."""
        # When later unwinding the block stack,
        # we need to keep track of why we are doing it.
        why = None
        try:
            bytecode_fn = getattr(self, f'byte_{byte_name}', None)
            if bytecode_fn is None:
                if byte_name.startswith('UNARY_'):
                    self.unaryOperator(byte_name[6:])
                elif byte_name.startswith('BINARY_'):
                    self.binaryOperator(byte_name[7:])
                else:
                    raise VirtualMachineError(
                        f"unsupported bytecode type:{byte_name}"
                    )
            else:
                why = bytecode_fn(*argument)
        except:
            # 处理执行该指令时遇到的异常
            self.last_exception = sys.exc_info()[:2] + (None,)
            why = 'exception'

        return why

    def run_frame(self, frame):
        """Run a frame until it returns (somehow).
                Exceptions are raised, the return value is returned.
        """
        self.push_frame(frame)
        while True:
            byte_name, arguments = self.parse_byte_and_args()

            why = self.dispatch(byte_name, arguments)

            # Deal with any block management we need to do
            while why and frame.block_stack:
                why = self.manage_block_stack(why)

            if why:
                break

        self.pop_frame()

        if why == 'exception':
            exc, val, tb = self.last_exception
            e = exc(val)
            e.__traceback__ = tb
            raise e

        return self.return_value



class Frame(object):
    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.global_names = global_names
        self.local_names = local_names
        self.prev_frame = prev_frame
        self.stack = []
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtins__']
            if hasattr(self.builtin_names, '__dict__'):
                self.builtin_names = self.builtin_names.__dict__

        self.last_instruction = 0
        self.block_stack = []


class Function(object):
    '''创造1个拟真的函数对象，按解释器的预期进行定义'''
    __slots__ = [
        'func_code', 'func_name', 'func_defaults', 'func_globals',
        'func_locals', 'func_dict', 'func_closure',
        '__name__', '__dict__', '__doc__',
        '_vm', '_func',
    ]

    def __init__(self, name, code, globs, defaults, closure, vm):
        self._vm = vm
        self.func_code = code
        self.func_name = self.__name__ = name or code.co_name
        self.func_defaults = tuple(defaults)
        self.func_globals = globs
        self.func_locals = self._vm.frame.f_locals
        self.__dict__ = {}
        self.func_closure = closure
        self.__doc__ = code.co_consts[0] if code.co_consts else None

        kw = {
            'argdefs': self.func_defaults,
        }
        if closure:
            kw['closure'] = tuple(make_cell(0) for _ in closure)
        self._func = types.FunctionType(code, globs, **kw)

    def __call__(self, *args, **kwargs):
        # 当调用一个函数时，创造一个新的帧并运行
        callargs = inspect.getcallargs(self._func, *args, **kwargs)
        # 使用callargs创造参数与值的映射并传入新的帧
        frame = self._vm.make_frame(
            self.func_code, callargs, self.func_globals, {}
        )
        return self._vm.run_frames(frame)


def make_cell(value):
    '''创造一个真实的python闭包 and grab a cell'''
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]
