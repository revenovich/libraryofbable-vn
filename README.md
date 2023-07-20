# Thư viện của Bable (Library of Bable)
## Thư viện của Bable là gì?
Thư viện của Bable là một truyện ngắn được viết bởi Jorge Luis Borges - một nhà văn người Argentina. Truyện được viết vào năm 1941. Truyện được viết bằng tiếng Tây Ban Nha và được dịch ra nhiều ngôn ngữ khác nhau.
## Tóm tắt nội dung truyện
Thư viện của Bable nói về một thư viện (có thể xem như là một vũ trụ) chứa tất cả các cuốn sách đã được viết, sẽ được viết và có thể là không bao giờ được viết. Ngoài ra có những cuốn sách chứa tất cả những gì thuộc về một cá thể như ngày tháng năm sinh, năm mất của họ, tất cả những gì họ đã nói và suy nghĩ trong cuộc đời.

Thư viện là một cấu trúc (gần như) vô tận, trong đó có những căn phòng hình lục giác. Vì là hình lục giác nên căn phòng có 6 bức tường, trong đó 2 bức tường sẽ là lối ra vào, 4 bức còn lại sẽ là tủ sách. Mỗi tủ sách sẽ có 5 giá sách, mỗi giá sách sẽ có 32 quyển sách và mỗi quyển sách có 410 trang. Trong một trang sách sẽ có 40 dòng, mỗi dòng có 80 kí tự và mỗi kí tự sẽ là một ký tự ngẫu nhiên trong bảng chữ cái Latinh (25 ký tự). Mọi cuốn sách đều giống nhau về cấu trúc.
## Thuật toán Thư viện của Babel online (https://libraryofbabel.info/)
Thuật toán của thư viện này được viết bởi Jonathan Basile. Thuật toán này sẽ tạo ra một thư viện ảo với cấu trúc giống như thư viện trong truyện. Mọi người có thể tìm hiểu thêm thông tin về thuật toán trong phần Theory của trang web.
## Triển khai thuật toán sử dụng python
Tác giả gốc của thuật toán sử dụng python được mình tìm thấy trên github của ([Louis](https://github.com/louis-e/LibraryOfBabel-Python)) và mọi giải thích của thuật toán đều được tác giả giải thích thông qua video ([youtube](https://youtu.be/I54-5E0r1f0)) này. Công việc của mình chỉ đơn giản là triển khai thêm bảng chữ cái tiếng việt vào thuật toán của tác giả cùng với một số thay đổi để phù hợp với bảng chữ cái tiếng việt.
## Tính năng của thuật toán
- Tìm kiếm một văn bản cụ thể và lấy địa chỉ có văn bản đó.
- Từ một địa chỉ bất kì, lấy ra văn bản tương ứng.
## Cách sử dụng
- Tải về và cài đặt python, khuyến khích sử dụng python có phiên bản từ 3.6 trở lên.
- Thay thế biến `search_term` bằng văn bản cần tìm kiếm.
- Hoặc thay thế biến `test_address` bằng địa chỉ cần tìm kiếm.