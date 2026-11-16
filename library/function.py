from functools import reduce


def normalize_text(text):
    """Membersihkan spasi dan menyeragamkan teks menjadi huruf kecil."""
    return " ".join(str(text).strip().lower().split())


def transform_data(data, function):
    """Menerapkan function pada setiap elemen; hasil baru dikembalikan."""
    return list(map(function, data))


def filter_data(data, predicate):
    """Memilih elemen yang memenuhi predicate."""
    return list(filter(predicate, data))


def aggregate_data(data, function, initial):
    """Menggabungkan elemen data menjadi satu nilai menggunakan reduce."""
    return reduce(function, data, initial)


def calculate_average(numbers):
    """Menghitung rata-rata tanpa mengubah data asli."""
    if not numbers:
        return 0
    total = aggregate_data(numbers, lambda accumulator, value: accumulator + value, 0)
    return total / len(numbers)


def sort_data(data, key_function, reverse=False):
    """Mengurutkan data dengan fungsi kunci yang diberikan sebagai argumen."""
    return sorted(data, key=key_function, reverse=reverse)


def search_data(records, keyword, field):
    """Mencari record yang mengandung keyword pada field tertentu."""
    normalized_keyword = normalize_text(keyword)
    return filter_data(
        records,
        lambda record: normalized_keyword in normalize_text(record.get(field, ""))
    )


def flatten_data(data):
    """Meratakan nested list secara rekursif."""
    if not isinstance(data, (list, tuple)):
        return [data]
    return aggregate_data(
        data,
        lambda result, item: result + flatten_data(item),
        []
    )