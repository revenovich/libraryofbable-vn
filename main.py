import random
import string

# Create charset with order numbers
# Mình quá lười để tạo charset bằng tay
# nhưng nhờ Copilot mà mình có thể tạo charset này :D
charset = {
    0: 'a',
    1: 'ă',
    2: 'â',
    3: 'b',
    4: 'c',
    5: 'd',
    6: 'đ',
    7: 'e',
    8: 'ê',
    9: 'g',
    10: 'h',
    11: 'i',
    12: 'k',
    13: 'l',
    14: 'm',
    15: 'n',
    16: 'o',
    17: 'ô',
    18: 'ơ',
    19: 'p',
    20: 'q',
    21: 'r',
    22: 's',
    23: 't',
    24: 'u',
    25: 'ư',
    26: 'v',
    27: 'x',
    28: 'y',
    29: ',',
    30: ' ',
    31: '.',
    32: 'á',
    33: 'à',
    34: 'ả',
    35: 'ã',
    36: 'ạ',
    37: 'ắ',
    38: 'ằ',
    39: 'ẳ',
    40: 'ẵ',
    41: 'ặ',
    42: 'ấ',
    43: 'ầ',
    44: 'ẩ',
    45: 'ẫ',
    46: 'ậ',
    47: 'é',
    48: 'è',
    49: 'ẻ',
    50: 'ẽ',
    51: 'ẹ',
    52: 'ế',
    53: 'ề',
    54: 'ể',
    55: 'ễ',
    56: 'ệ',
    57: 'í',
    58: 'ì',
    59: 'ỉ',
    60: 'ĩ',
    61: 'ị',
    62: 'ó',
    63: 'ò',
    64: 'ỏ',
    65: 'õ',
    66: 'ọ',
    67: 'ố',
    68: 'ồ',
    69: 'ổ',
    70: 'ỗ',
    71: 'ộ',
    72: 'ớ',
    73: 'ờ',
    74: 'ở',
    75: 'ỡ',
    76: 'ợ',
    77: 'ú',
    78: 'ù',
    79: 'ủ',
    80: 'ũ',
    81: 'ụ',
    82: 'ứ',
    83: 'ừ',
    84: 'ử',
    85: 'ữ',
    86: 'ự',
    87: 'ý',
    88: 'ỳ',
    89: 'ỷ',
    90: 'ỹ',
    91: 'ỵ',
    92: ',',
    93: ' ',
    94: '.',
}
charset_length = len(charset)

# max_page_content_length là 3200 ký tự trong 1 trang sách
# 80 kí tự cho 1 dòng, 40 dòng cho 1 trang
# Có thể tăng hoặc giảm max_page_content_length để tăng hoặc giảm độ dài của trang sách
# nhưng sẽ ảnh hưởng đến độ dài của hexagon address và tốc độ tìm kiếm
# Mặc định mình để là 3200, theo truyện ngắn
max_page_content_length = 3200

# max_walls, max_shelves, max_volumes, max_pages là số lượng tối đa của từng loại
# Những thông số này đều ảnh hưởng đến độ dài của hexagon address và tốc độ tìm kiếm tương tự như max_page_content_length
# Mình để mặc định là 4, 5, 32, 410 đều theo truyện ngắn
max_walls = 4
max_shelves = 5
max_volumes = 32
max_pages = 410

# Tạo ngẫu nhiên wall, shelf, volume, page
wall = str(random.randint(1, max_walls))
shelf = str(random.randint(1, max_shelves))
volume = str(random.randint(1, max_volumes)).zfill(2)
page = str(random.randint(1, max_pages)).zfill(3)

# Tính toán library_coordinate từ wall, shelf, volume, page
library_coordinate = int(page + volume + shelf + wall)

# hexagon_base là cơ số của hexagon address
# 36 là từ số kí tự từ 0-9 và a-z
hexagon_base = 36

# Tìm kiếm hexagon address từ page content
def searchByContent(text: str, library_coordinate):
    text = ''.join([c for c in text.lower() if c in charset.values()])
    text = text.rstrip().ljust(max_page_content_length, ' ')
    sum_value = 0
    # Sum value of each character in text
    for i, c in enumerate(text[::-1]):
        # check if c is a character
        if c.isalpha():
            # get the order number of c in charset
            char_value = list(charset.keys())[list(charset.values()).index(c)]
        elif c == ',':
            char_value = 92
        elif c == '.':
            char_value = 94
        else:
            char_value = 93
        sum_value += char_value * (charset_length**i)

    result = library_coordinate * (charset_length**max_page_content_length) + sum_value
    result = convertToBase(result, hexagon_base)
    return result

# Tìm kiếm page content từ hexagon address
def searchByAddress(address):
    hexagon_address, wall, shelf, volume, page = address.split(':')
    volume = volume.zfill(2)
    page = page.zfill(3)
    library_coordinate = int(page + volume + shelf + wall)

    seed = int(hexagon_address, hexagon_base) - library_coordinate * (charset_length**max_page_content_length)
    hexagon_base_result = convertToBase(seed, hexagon_base)
    result = convertToBase(int(hexagon_base_result, hexagon_base), charset_length)

    if len(result) < max_page_content_length:
        random.seed(result)
        while len(result) < max_page_content_length:
            result += charset[int(random.random() * len(charset))]
    elif len(result) > max_page_content_length:
        result = result[-max_page_content_length:]
    return result

# Hàm chuyển đổi ra hexagon address
def convertToBase(x, base):
    if base == 36: digs = string.digits + 'abcdefghijklmnopqrstuvwxyz'
    elif base == 10: digs = '0123456789'
    elif base == 60: digs = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    else: digs = charset

    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1

    x *= sign

    chars = []
    while x:
        chars.append(digs[x % base])
        x //= base
    if sign < 0:
        chars.append('-')

    chars.reverse()
    return ''.join(chars)

#Page content to hexagon address example
search_term = "Đây là nội dung của trang sách"
hexagon_address = searchByContent(search_term, library_coordinate)
total_address = hexagon_address + ':' + wall + ':' + shelf + ':' + volume + ':' + page
print("Hexagon address:", total_address)

#Hexagon address to page content example
contentByAddress = searchByAddress(total_address)
print("Page content:", contentByAddress.rstrip())

#Test
test_address = "1camfn2vymt10qoba1l0sx3k77ejs5rjrkx7csj7be80x5xi2uapmb7rjvvkmgjnta9yzym1inuw354qzglh1bktcfds6y5ov87swcj0fcd25sfx2ds5t8klalgcp36aliag6wz4gtyohee2ufyfr3rz864a9c7xfwy4764pxluvjbpcomqztund5hvay0y79notyjget8399cmhv5l3vpcwazr5b56sant0lbm69mfisn6fa70czhd7xua54pxm2rzcls4cog2g7mc0pzbs9luiibjzu3c5m8nyb3si1p7i0ez9wadhaprh1g37bm6kyg8kc4ny1m7v5fagbo58xyze115ev54z3d44vztt0hgax0g8yuq7n2c3bnl92wimq1opowmmn9fxm5jrq5u2muzkf6lx7vth3we3cwtw8aerz5zrmnp4wu9kwuboh7v24mlkjh5d414cvr5lxdjuqw4s0wd65v789pxkgyap3owzgqj41ohgjjuk9kmzbnlw1tz292dy5mlrxd04yh5bzg64uicdzho7mzxr6ntun18mjnm90l12vzbuvnz75av7piaczcl5vwlqv6uxdhkqdvaa4l5woysvmyoivsharwf9fnxktaiji8ci6xhu3qf39qsqmi0wnlg1or9y4oiisno3sluicahvqo8a1n1ms1mr1g8w98v4hijf0uczguoke7bqp1s8mpf1txleqt65zuagpq70247qsu2il99ba5lii6tjjhaf5zwm154tqpgiy9rgsfy1c354nrpr1gwvqyom53zq1pbruf9fxmkibftcsowpkpjur5zo19d42j66sw171ju828b63hnd84gma9azrf5c82z4jvpm576ab1gzz348qjet12r6tzs6ba49rbs6m8ky03k8w5dha1o60sidr3jd54e3r9xgq3czci7g91cc5dnh90pgqlav7cwtwfm6m7utuwxlobg5kz0gc77rp2r7nxi7o2eu0u2zpocn5eva0ywjpdyqwmo1uw3q720hay98ur3a0mxas6qwii39ci1q3583cbafjucom9j42kjdzwgcrsegck43jd8kgdv90mn7a4x0258czqees24vpd8desfekgkxs4yg25f6iy8nvhfrdx6p01dh3wywn0rhy78uds29f1jb5kksrhu75hqjnf9744pdfrkcu25p653br95u01f639nbg0c06iqhqsoa0x9dufptf9ykekxnjbpt5lndakkgyyg1esbmw9w00jv9yeqvztmrjlujdzh4lrew727go0x0ev8jbnarrwdnkxcfn47z725l0xo648xo6j1m6sz6zlvhbd37om0e2sc0ahgky87jancewkj9rkoqpxbh6mkc2cl2wyhb5nekzlglusgibeqv54w1z2xdxfbtb798oorgln7hviqh9viyt9vcu4i9xm85i48dm796akekgr086ixybdakqobp9t9qq7k8covm50qcwungwb1a26i8gqfzxe31sgbz0flhdrel4s8aih6a5mfoh5sufkogokyx5v753xu5hfbuayktr861nhxfcgcobtpsdpl72cqb5fj9ljzj0rcfdtpd2079qsmcshekty6obfa2jcugfr50yh5uvpqi2ajxq95rznmivurn84ozoxox7ov324feg58hqomyxwasg9d23rat5ujxkbvsbolhpjdp7jbl0d27nnossx8jycw2o20pnegggvlm1l03il1eth22wblypwf61syqmnkb0ldfe6zbr3wnun708dic3eadopjwdsnx76ub89xxzoq1lbgb2ezh4fgrap3uc7q12tsvgyxi93gtn4upr95ibseza31c3ipckquzxeo646h15jv43v8m2v7eb5gky6c52hl4a16z1540c0nqo2ux3bmpxw8ofv7pt2ukl7jnlhf0zh4rhs0yv2ca4bs05lscdsg5wkn19x69kyasr6f9e2cwunai75erzr5x6cihzx1yqequhvdqcoqlgi5v68fspsjo0wway1avfeq91hb28wjr09kmwe2hi6t9tqdbhsb53x83ftmr9imqm3uveyrongelsqt3f7hmg2lem5wzwe8cc3uwdnuoml56x3otoxsc500i87b5s9yqj8mcn1t8ll9ihp0kaa8vjhgade55selxzqkhov8qptic5sax2o28oc3uve4v35afu773ahzhooj5ulz9yjhj1ox99544o1vnqep574wtjfkl0hjgufj91jrk599si33w5ow23zhjwdstwe0mejvr7ob0bts8u15wejcaw4aj56rl6rqc40dc4h0sxg53m6w07dur4n0jaf4vvbx4bdo3dezlvtvhgm9zhioyiqhdqekseiijpcobfmrxnsc3yjhj6q7ug2m5ujsqlzhr7kfoadcievnq08hlu0falkqex54nmln4s38lqzzf11uohwx3sm1521orj3i3xtfbh1ybx3ztaegyrx4vljyywovzsul3sikuwzjbqswinexdw1wk8878v0tqq6c8fxz2r8v45tk5zygoxy9fhs599cttjfcwqfagt6nvucgk6sb9no2wjpfy73wmwy7xa5e07mm1o0zomiqgbd9a6glfirqkjc9ur1dnxcyfuilp0l6nhw9ktwh2umjjqdljh7o1ilibm4a8rxfs5i6ed95knqih7v8vw6pjb1ygmb0kdg9do21wh5bvawbgxvg35f43s7o40ysit58hpmdow8890sh4n6jwu5qfjmt8kvy8xbqv0cjf7fiekwse2sdrqvz8bftmkpjxe0g5kr743epdexbd36k7rkj96612xl8hh2qqm3molkfen0jfjccuo4tuqd3cizvd33gfnpphladwdhiu48j5a8shq1to4o4vyfbtf56av79yqdzdxuw9hym6bc9lrzq5umm1g3d1zklh51qtokl1qad69c0qevwbccabh6i7epa94hi9th41xfhd6iioxflmfd1zkdpli8ht875gv10pxzj6o1j1slzyp75pi1efc01kcw7l6rwyam64d2lwibq5mfnahg7dev9vlpgue7rvho3tpkckdth6erji8mfd6pggt7hyds7p4eamhlsubinjlfcq1aaj3xsfodukgjockk9esgn0i394h33clblwss4wweuau1xadr35cqwcgd5hp4zez18028ak5d7fe2fdn7sxaab3ruyy5kmneldlujig1tldl6r5ntc24lhxyn7uibvqlgqci07kiyro8wzq22nowhqd9l6guk34cghq00mkucnt52ynugbha0kh88bulglvp36v2sltv24tp3cffhdgjizf74yfekysh2obnezycnomdi04h3i03wcq0k26putq3ku2ljtklr1odal5dd4vo6gaeu3lqm34xundcjur88ga3z0sbbhudhkjlvb49va2nkflpied882o791z6yegsz4vl46k0tu0bdp4ijoi7il5e8jaby8b9a75obkzeoc9zn0p77vm7gebu0glac30npdgbt8vvieo5aq7uzd6bzfbsng9nd5qnej5r1oxpeoym0ww7tcbc35bry78b0r98gjbviw47hv6t11muffajiqtdncdxlaw0x44l6ub34riwmmvixulkg42rbyn0uc16rr1j31zf0b3y6ccsun6r2gme2hx5dqmine5s4dme1zal61xu11iifbrf21ffhtkk4ldcp704wlaweum1m5g7wjqctw88wr4vp5t92h4oves4wxhxhd756sgkgtiln36olq0nzd7bydwqighedoa2048efsf3j713qijybx0cdfl5iwenrufiidm9d3tk86921qw9dyq7mpvp9l484rkhoy32pqaxlree4czee8j23gexbd5uprl871sq92z8b6irg1m9t6ywxiaf11yoh91v0cudu9ps0hfms42m2dcl8axxml8xz0u4g0fxldcg3mcu6mzdlyaaon3ogu7s1ndpmd1t530ystiuwzja0848z2w3om1pq9ufv7i7x7m5sovv2n6cv8of9glauehqetb9r:1:6:01:001"
contentByAddress = searchByAddress(test_address)
print("Page content:", contentByAddress.rstrip())