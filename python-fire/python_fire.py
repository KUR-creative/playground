import fire

class interface:
    @staticmethod
    def test(a, b, c, why):
        print(a,b,c, why)
        return a + b + c

if __name__ == '__main__':
    fire.Fire(interface)
