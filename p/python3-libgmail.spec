%define oname libgmail

Summary: Python bindings to access Gmail
Name: python3-%oname
Version: 0.1.11
Release: 1
Source0: https://downloads.sourceforge.net/libgmail/%{oname}-%{version}.tar.gz
License: GPL
Group: Development/Python
URL: https://libgmail.sourceforge.net/
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-mechanize
Requires: python3-mechanize

%description
This is a Python library to access Google Mail.

%prep
%setup -q -n %oname-%version
sed -i -e 's|email.MIMEBase|email.mime.base|' -e 's|email.MIMEText|email.mime.text|' -e 's|email.MIMEMultipart|email.mime.multipart|' libgmail.py
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|/usr/bin/env python|/usr/bin/python3|' *.py

%build
python3 setup.py build

%install
python3 setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python3_sitelib}/*

%changelog
* Wed Nov 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.11
- Rebuilt for Fedora
* Fri Nov 04 2011 Götz Waschk <waschk@mandriva.org> 0.1.11-5mdv2012.0
+ Revision: 717571
- rebuild
* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.1.11-4mdv2011.0
+ Revision: 592879
- rebuild for new python 2.7
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.11-3mdv2011.0
+ Revision: 442246
- rebuild
* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.11-2mdv2009.1
+ Revision: 319533
- rebuild with python 2.6
* Sun Nov 09 2008 Götz Waschk <waschk@mandriva.org> 0.1.11-1mdv2009.1
+ Revision: 301341
- new version
- update file list
* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 0.1.10-2mdv2009.0
+ Revision: 250696
- new version
- update deps
* Sat May 03 2008 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2009.0
+ Revision: 200761
- new version
- depend on ClientCookie
  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 0.1.8-1mdv2008.1
+ Revision: 108688
- new version
* Tue Oct 09 2007 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2008.1
+ Revision: 95773
- new version
* Fri Jan 19 2007 Götz Waschk <waschk@mandriva.org> 0.1.5.1-1mdv2007.0
+ Revision: 110835
- Import python-libgmail
* Fri Jan 19 2007 Götz Waschk <waschk@mandriva.org> 0.1.5.1-1mdv2007.1
- initial package
