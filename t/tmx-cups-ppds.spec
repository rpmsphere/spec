Name:		tmx-cups-ppds
Version:	2.0.3.0
Release:	1.bin
Summary:	TM/BA Series Printer Driver CUPS ppds
License:	Epson non-free proprietary license
Group:		Applications/System
URL:		https://www.epson-biz.com/modules/pos/index.php?page=single_soft&cid=5012
Source0:	%{name}.zip
BuildArch:	noarch
Requires:	tmx-cups

%description
These are CUPS ppds for TM/BA Series.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/ppd/Epson
install -m644 *.ppd.gz %{buildroot}%{_datadir}/ppd/Epson

%clean
rm -rf %{buildroot}

%files
%{_datadir}/ppd/Epson/tm-*.ppd.gz

%changelog
* Tue Apr 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3.0
- Initial package
