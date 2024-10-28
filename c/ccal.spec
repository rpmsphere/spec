%undefine _debugsource_packages

Name:       ccal
License:    GPL, portions LGPL
Group:       Utilities/System 
Version:      2.5.3
Release:      4.1
URL:         https://ccal.chinesebay.com/ccal/index.html
Summary:     Display a calendar together with Chinese calendar
Source:       https://ccal.chinesebay.com/ccal/%{name}-%{version}.tar.gz 
Patch0:       ccal-2.5.3-make.patch

%description
The ccal utility writes a Gregorian calendar together with
Chinese calendar to standard output.

Authors:
--------
Zhuo Meng <zxm8@case.edu>

%prep
%setup -q
%patch 0 -p0

%build
make

%install
rm -rf $RPM_BUILD_ROOT
export _bindir=$RPM_BUILD_ROOT%{_bindir}
make install
export _mandir=$RPM_BUILD_ROOT%{_mandir}
make install-man

%files
%doc ChangeLog COPYING COPYING.LESSER README
%doc %{_mandir}/man1/ccal.1.gz
%doc %{_mandir}/man1/ccalpdf.1.gz
%attr(0755, root, root) %{_bindir}/ccal
%attr(0755, root, root) %{_bindir}/ccalpdf

%changelog
* Sat Aug 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.3
- Rebuilt for Fedora
* Sun Mar 04 2012 - Zhuo Meng <zxm8@case.edu>
- Updated for version 2.5.3
* Mon Oct 05 2009 - Zhuo Meng <zxm8@case.edu>
- Updated for version 2.5.2
* Sat Aug 15 2009 - Zhuo Meng <zxm8@case.edu>
- Updated for version 2.5.1
* Fri Jul 25 2008 - Zhuo Meng <zxm8@case.edu>
- Updated for version 2.5
* Sun Mar 26 2006 - Zhuo Meng <zhuo@thunder.cwru.edu>
- Updated for version 2.4
* Tue Jul 06 2004 - Zhuo Meng <zhuo@thunder.cwru.edu>
- Updated for version 2.3.3
* Sat Jun 12 2004 - Zhuo Meng <zhuo@thunder.cwru.edu>
- Updated for version 2.3.2
* Mon Oct 20 2003 - Zhuo Meng <zhuo@thunder.cwru.edu>
- Updated for version 2.3.1
* Sun Sep 28 2003 - Zhuo Meng <zhuo@thunder.cwru.edu>
- Updated for version 2.3
* Mon Jun 30 2003 - Wei He <hewei@ied.org.cn>
- Packaged into a RPM
