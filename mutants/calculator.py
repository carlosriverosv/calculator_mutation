from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict

mutants_xǁCalculatorǁadd__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalculatorǁsubtract__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalculatorǁmultiply__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalculatorǁdivide__mutmut: MutantDict = {}  # type: ignore


class Calculator:
    @_mutmut_mutated(mutants_xǁCalculatorǁadd__mutmut)
    def add(self, a, b):
        return a + b

    def xǁCalculatorǁadd__mutmut_orig(self, a, b):
        return a + b

    def xǁCalculatorǁadd__mutmut_1(self, a, b):
        return a - b

    @_mutmut_mutated(mutants_xǁCalculatorǁsubtract__mutmut)
    def subtract(self, a, b):
        return a - b

    def xǁCalculatorǁsubtract__mutmut_orig(self, a, b):
        return a - b

    def xǁCalculatorǁsubtract__mutmut_1(self, a, b):
        return a + b

    @_mutmut_mutated(mutants_xǁCalculatorǁmultiply__mutmut)
    def multiply(self, a, b):
        return a * b

    def xǁCalculatorǁmultiply__mutmut_orig(self, a, b):
        return a * b

    def xǁCalculatorǁmultiply__mutmut_1(self, a, b):
        return a / b

    @_mutmut_mutated(mutants_xǁCalculatorǁdivide__mutmut)
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def xǁCalculatorǁdivide__mutmut_orig(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def xǁCalculatorǁdivide__mutmut_1(self, a, b):
        if b != 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def xǁCalculatorǁdivide__mutmut_2(self, a, b):
        if b == 1:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def xǁCalculatorǁdivide__mutmut_3(self, a, b):
        if b == 0:
            raise ZeroDivisionError(None)
        return a / b

    def xǁCalculatorǁdivide__mutmut_4(self, a, b):
        if b == 0:
            raise ZeroDivisionError("XXCannot divide by zeroXX")
        return a / b

    def xǁCalculatorǁdivide__mutmut_5(self, a, b):
        if b == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return a / b

    def xǁCalculatorǁdivide__mutmut_6(self, a, b):
        if b == 0:
            raise ZeroDivisionError("CANNOT DIVIDE BY ZERO")
        return a / b

    def xǁCalculatorǁdivide__mutmut_7(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a * b


mutants_xǁCalculatorǁadd__mutmut["_mutmut_orig"] = Calculator.xǁCalculatorǁadd__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁCalculatorǁadd__mutmut["xǁCalculatorǁadd__mutmut_1"] = Calculator.xǁCalculatorǁadd__mutmut_1  # type: ignore # mutmut generated

mutants_xǁCalculatorǁsubtract__mutmut["_mutmut_orig"] = Calculator.xǁCalculatorǁsubtract__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁCalculatorǁsubtract__mutmut["xǁCalculatorǁsubtract__mutmut_1"] = Calculator.xǁCalculatorǁsubtract__mutmut_1  # type: ignore # mutmut generated

mutants_xǁCalculatorǁmultiply__mutmut["_mutmut_orig"] = Calculator.xǁCalculatorǁmultiply__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁCalculatorǁmultiply__mutmut["xǁCalculatorǁmultiply__mutmut_1"] = Calculator.xǁCalculatorǁmultiply__mutmut_1  # type: ignore # mutmut generated

mutants_xǁCalculatorǁdivide__mutmut["_mutmut_orig"] = Calculator.xǁCalculatorǁdivide__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_1"] = Calculator.xǁCalculatorǁdivide__mutmut_1  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_2"] = Calculator.xǁCalculatorǁdivide__mutmut_2  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_3"] = Calculator.xǁCalculatorǁdivide__mutmut_3  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_4"] = Calculator.xǁCalculatorǁdivide__mutmut_4  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_5"] = Calculator.xǁCalculatorǁdivide__mutmut_5  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_6"] = Calculator.xǁCalculatorǁdivide__mutmut_6  # type: ignore # mutmut generated
mutants_xǁCalculatorǁdivide__mutmut["xǁCalculatorǁdivide__mutmut_7"] = Calculator.xǁCalculatorǁdivide__mutmut_7  # type: ignore # mutmut generated
