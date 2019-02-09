import time


def debug(func):

  def wrapper(*args, **kwargs):
    start_time = time.time()

    result = func(*args, **kwargs)

    end_time = time.time()

    print func.__module__, func.__name__, 'executed in', (end_time - start_time)
    print '  result: ', result, ' args: ', args, ' kwargs: ', kwargs

    return result

  return wrapper


@debug
def spam(name, retries=5):
  print 'spam'

  result = name
  for i in range(retries):
      result = hash(result)

  return result


if __name__ == '__main__':
  spam('Ivan')
  spam('Boris', retry=0)
  spam('Vitaly')
