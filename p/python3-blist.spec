%global srcname blist

Name:           python3-%{srcname}
Version:        1.3.6
Release:        24
Summary:        Faster list implementation for Python
License:        BSD
URL:            http://pypi.python.org/pypi/blist/
Source0:        http://pypi.python.org/packages/source/b/blist/blist-%{version}.tar.gz
# https://github.com/DanielStutzbach/blist/pull/78
Patch0001:      0001-Fix-compatibility-for-Python-3.7.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc

%description
The blist is a drop-in replacement for the Python list that provides
better performance when modifying large lists. The blist package also
provides sortedlist, sortedset, weaksortedlist, weaksortedset,
sorteddict, and btuple types.

Python's built-in list is a dynamically-sized array; to insert or
remove an item from the beginning or middle of the list, it has to
move most of the list in memory, i.e., O(n) operations. The blist uses
a flexible, hybrid array/tree structure and only needs to move a small
portion of items in memory, specifically using O(log n) operations.

For small lists, the blist and the built-in list have virtually
identical performance.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install
 
%files
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/

%changelog
* Fri Jan 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.6-24
- Rebuilt for Fedora
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Thu Nov 07 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-23
- Subpackage python2-blist has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-22
- Rebuilt for Python 3.8.0rc1 (#1748018)
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-21
- Rebuilt for Python 3.8
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.3.6-18
- Rebuild with fixed binutils
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-16
- Rebuilt for Python 3.7
* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.6-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.6-13
- Python 2 binary package renamed to python2-blist
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-9
- Rebuild for Python 3.6
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4
* Thu May  8 2014 Michel Salim <salimma@fedoraproject.org> - 1.3.6-1
- Update to 1.3.6
- Build for Python 3 as well on supported releases
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Sat Jul  2 2011 Michel Salim <salimma@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Mon Jul 26 2010 Michel Salim <salimma@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
* Fri May 21 2010 Michel Salim <salimma@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1
* Fri Oct 23 2009 Michel Salim <salimma@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2
* Sat Oct 10 2009 Michel Salim <salimma@fedoraproject.org> - 1.0.1-1
- Initial package
