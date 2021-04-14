Summary: Generic Coco/R and CocoXml for multi-languages
Name: cocoxml
Version: 0.9.2
Release: 10.2
License: GPL
Group:  Development/Tools
Source0: http://cocoxml.googlecode.com/files/%{name}-%{version}.tar.gz
URL: http://code.google.com/p/cocoxml/
BuildRequires: python2-scons

%description
CocoXml is inspired by Coco/R and modified from it. The new implemented
Coco(in c) and CocoXml are combined into one binary. If the extension of
the input is .atg, it is treated as a syntax of the original Coco. If the
extension of the input is .xatg, it is treated as a syntax of CocoXml.

%prep
%setup -q

%build
python2 configure.py --prefix=/usr
scons

%install
rm -rf $RPM_BUILD_ROOT
python2 install.py DESTROOT=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/Coco
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/Coco
%{_datadir}/Coco
%{_includedir}/Coco
%{_libdir}/libcoco.a
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.2
- Rebuilt for Fedora
