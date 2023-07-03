%define	fontdir	%{_datadir}/fonts/taiwan

Summary: Taiwan Fonts
Name: taiwan-fonts
Version: 3.10
Release: 1
License: freeware
Group: User Interface/X
BuildArch: noarch
Source0: taiwan-fonts.zip
URL: https://wesingkasu.blogspot.tw/2012/01/blog-post_1223.html
Requires(post): fontconfig

%description
Based on Taiwan MOE standard Fonts with more local glyphs.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m 0644 * %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%{fontdir}/*

%changelog
* Wed Mar 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.10
- Rebuilt for Fedora
