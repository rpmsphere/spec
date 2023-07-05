%undefine _debugsource_packages
%define tarname pyFltk

Summary:	Python wrapper for the FLTK library
Name:		pyfltk
Version:	1.3.5
Release:	1
Source0:	https://downloads.sourceforge.net/pyfltk/%{tarname}-%{version}.tar.gz
Patch0:		pyFltk-1.3.0rc1-build.patch
License:	GPLv2
Group:		Development/Python
URL:		https://pyfltk.sourceforge.net/
BuildRequires:	fltk-devel, mesa-libGL-devel
BuildRequires:	python3-devel
BuildRequires:	gcc-c++, swig

%description 
pyFLTK is a Python wrapper for the Fast Light Tool Kit
cross-platform graphical user-interface library.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1 -b .cflags

# (wally) With P0, disable Werror_cflags temporarily to get pkg build
%define Werror_cflags   %nil
sed -i -e 's|@MGA_CFLAGS@|%{optflags} -Wno-format-security|' setup.py

%build
CPPFLAGS="-DFL_INTERNALS %optflags -Wno-format-security" python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{python3_sitearch}/fltk/docs
rm -rf $RPM_BUILD_ROOT%{python3_sitearch}/fltk/test
sed -i 's|exec line|exec(line)|'  %{buildroot}%{python3_sitearch}/python/updateInits.py

%files
%doc CHANGES COPYING README
%{python3_sitearch}/fltk
%{python3_sitearch}/*info
%{python3_sitearch}/python

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.5
- Rebuilt for Fedora
* Thu Jan 26 2012 fwang <fwang> 1.3.0-1.mga2
+ Revision: 202024
- update doc list
- 1.3.0 final
- update tarball
- br swig
- regenerate wrapper
- new version 1.3.0 rc1
  + wally <wally>
    - add P0 to disable Werror_cflags temporarily to get pkg build
    - use correct CPPFLAGS to get pkg build
* Sun Apr 24 2011 grenoya <grenoya> 1.1.3-2.mga1
+ Revision: 90154
- imported package python-pyfltk
