%global debug_package %{nil}

Name:         rebol3
Summary:      REBOL language
URL:          http://www.rebol.com/
Group:        Development/Language
License:      Apache License 2.0
Version:      2.101.0
Release:      22.1
#Source0:      https://github.com/rebol/rebol
Source0:      r3-prepared.zip

%description
REBOL is not a traditional computer language. It's not for everyone.
It's for thinkers and doers -- those who want more power and flexibility
in their language, and those who want to solve computing problems
in smarter more elegant ways.

%prep
%setup -q -n r3-master
sed -i 's|-m32|-fPIC -Wl,--allow-multiple-definition|' make/makefile
mkdir -p make/objs

%build
make -C make lib top

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 make/r3 $RPM_BUILD_ROOT%{_bindir}/rebol3
install -Dm755 make/libr3.so $RPM_BUILD_ROOT%{_libdir}/librebol3.so

%files
%doc LICENSE NOTICE README
%{_bindir}/rebol3
%{_libdir}/librebol3.so

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Dec 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.101.0
- Rebuild for Fedora
