if __name__ == "__main__":
    import sys
    print(type(sys.path))
    for env in sys.path:
        print(env)
