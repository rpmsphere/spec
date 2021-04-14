%define __python /usr/bin/python2
Summary: A simple, transparent and easy to extend xorg parser
Name:    python-xkit
Version: 0.5.0
Release: 5.1
Source0: https://launchpadlibrarian.net/107156275/x-kit_%{version}.tar.gz
License: LGPLv2
Group:   Development/Libraries
URL:     https://launchpad.net/x-kit
BuildRequires: python-devel
BuildArch: noarch

%description
A simple, transparent and easy to extend xorg parser.

%prep
%setup -q -n xorgparser
chmod -x tests/* examples/*


%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --skip-build  --root $RPM_BUILD_ROOT 
ln -s xkit %{buildroot}%{python_sitelib}/XKit

%files 
%doc AUTHORS COPYING README PKG-INFO examples tests
%{python_sitelib}/*

%changelog
* Mon Feb 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Sun Mar 27 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.2.2-1
- https://launchpad.net/xorgparser/+announcement/5638
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Jul 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.2-6
- Fix egginfo location for Python-2.7 rebuild
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Sun Oct 25 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.4.2-4
- Fix FTBFS: fixed %%files section for python 2.6
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Fri Apr 10 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.2-2
- Fix review issues
* Tue Apr 07 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.4.2-1
- Initial spec file
