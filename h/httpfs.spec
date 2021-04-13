Name:           httpfs
Version:        2.06.07.10
Release:        4
Summary:        HTTP fuse filesystem
License:        GPLv2
Group:          Networking/Remote access
URL:            http://httpfs.sourceforge.net/
Source0:        %{name}_%{version}.tar.bz2
Patch0:         %{name}-2.06.07.10-magos-hostnames.patch
BuildRequires:  pkgconfig(fuse)

%description
httpfs is useful for mounting iso images over HTTP.

%prep
%setup -q -c
%patch0 -p0
rm -f %{name}
chmod -x %{name}.c
sed -i "s|-D_SVID_SOURCE -D_BSD_SOURCE|-D_DEFAULT_SOURCE|g" ./make_%{name}
sed -i "s|gcc -s|gcc|g" ./make_%{name}
sed -i "s|MagOS|Mageia|g" ./%{name}.c
iconv -f iso8859-15 -t utf-8 readme.1 > readme.1.conv && mv -f readme.1.conv readme.1

%build
./make_%{name}

%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc readme readme.1
%{_bindir}/%{name}

%changelog
* Sat Apr 3 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.06.07.10
- Rebuild for Fedora
* Fri Feb 14 2020 umeabot <umeabot> 2.06.07.10-4.mga8
+ Revision: 1522601
- Mageia 8 Mass Rebuild
* Mon Jan 28 2019 alexl <alexl> 2.06.07.10-3.mga7
+ Revision: 1361763
- s/MagOS/Mageia/
* Mon Jan 28 2019 alexl <alexl> 2.06.07.10-2.mga7
+ Revision: 1361549
- fix debug pkg generation
* Mon Jan 28 2019 alexl <alexl> 2.06.07.10-1.mga7
+ Revision: 1361543
- imported package httpfs
