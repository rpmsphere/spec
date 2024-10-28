%define oname   EditObj2

Name:           python2-editobj2
Summary:        Tkinter dialog box for editing any Python object
Version:        0.4
Release:        7.1
Source:         %{oname}-%{version}.tar.gz
URL:            https://home.gna.org/oomadness/en/editobj/
License:        GPLv2
Group:          Development/Python
BuildRequires:  python2-devel
Requires:       tkinter
Obsoletes:      editobj
BuildArch:      noarch

%description
EditObj2 can create and display a Tkinter dialog box for editing any Python
object (similarly to what Java call a Bean editor, but for Python object).
EditObj2 is a useful tool for writing (text or non-text) editors of all
kinds, including GUI editor, 3D editor,... It also includes a Python console.

EditObj2 supports also lists, dictionaries and hierarchies (nested lists)
edition. EditObj2 includes also a tree widget for Tkinter, an event framework
and a mutiple undo/redo system.

%prep
%setup -q -n %{oname}-%{version}

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --root=%{buildroot}

%files
%doc AUTHORS LICENSE README 
%python2_sitelib/*

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Tue Oct 22 2013 umeabot <umeabot> 0.4-4.mga4
+ Revision: 542620
- Mageia 4 Mass Rebuild
* Mon Oct 14 2013 pterjan <pterjan> 0.4-3.mga4
+ Revision: 497733
- Rebuild to add different pythonegg provides for python 2 and 3
* Fri Jan 11 2013 umeabot <umeabot> 0.4-2.mga3
+ Revision: 349501
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Mon Sep 19 2011 obgr_seneca <obgr_seneca> 0.4-1.mga2
+ Revision: 145397
- new version 0.4
* Tue Jul 12 2011 stormi <stormi> 0.2.1-3.mga2
+ Revision: 123459
- increase release so that it's higher than in Mageia 1
* Thu Jun 23 2011 zezinho <zezinho> 0.2.1-2.mga2
+ Revision: 112836
- spec cleanup for first build
  + kharec <kharec>
    - imported package editobj2
* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.2.1-2mdv2011.0
+ Revision: 590801
- rebuild for py2.7
* Sun Apr 18 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2.1-1mdv2010.1
+ Revision: 536464
- import editobj2
