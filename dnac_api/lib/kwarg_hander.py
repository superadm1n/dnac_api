def handle_kwargs(params, allowed_kwargs, **kwargs):
    if kwargs:
        for key, value, in kwargs.items():
            if key not in allowed_kwargs:
                raise KeyError('URL parameter {} not allowed, please use one of the following {}'.format(key, ', '.join(allowed_kwargs)))
            params[key] = value
    return params