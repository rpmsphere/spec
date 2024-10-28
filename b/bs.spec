Summary: A compiler/interpreter for modest-sized programs
Name: bs
Version: 1.3
Release: 1
License: free
Group: Development/Language
URL: https://en.wikipedia.org/wiki/Bs_(programming_language)
#SOURCE: https://minnie.tuhs.org/cgi-bin/utree.pl?file=pdp11v/usr/src/cmd/bs/
Source0: %{name}-%{version}.zip
Patch0: %{name}-1.3-dirty-hack.patch

%description
bs is a remote descendant of Basic [sic] and SNOBOL4, with a little C thrown in.

%prep
%setup -q
%patch 0 -p 1
sed -i 's|-O -g|-O -g -fPIE|' bs.mk

%build
make -f bs.mk

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc testall
%{_bindir}/%{name}

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
