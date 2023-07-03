Name:           python2-gtkmvc
Summary:        Multiplatform implementation of a dialect of the Model-View-Controller and Observer patterns for the PyGTK2
Version:        1.2.2
Release:        1
License:        BSD
Group:          Development/Libraries/Python
Source:         https://ovh.dl.sourceforge.net/sourceforge/pygtkmvc/python-gtkmvc-%{version}.tar.gz
URL:		https://sourceforge.net/projects/pygtkmvc/
BuildArch:      noarch
Requires:       pygtk2, libglade2
BuildRequires:  libglade2-devel, pygtk2-devel

%description
Pygtk MVC is a multiplatform implementation of a dialect
of the Model-View-Controller and Observer patterns for the
PyGTK2 toolkit.

MVC is a pattern that can be successfully used to design
and develop well structured GUI applications.
The MVC pattern basically helps in separating sematics
and data of the application, from their representation.

Within Pygtk MVC the Observer pattern is also embedded.
This pattern allows making separated parts independent,
but still connected each other.

%prep
%setup -q -n python-gtkmvc-%{version}
sed -i 's/python2\.4/python2/' examples/mini-yoman/yoman

%build
export CFLAGS="$RPM_OPT_FLAGS"
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%doc docs examples AUTHORS COPYING INSTALL NEWS README PKG-INFO
%{_bindir}/gtkmvc-progen
%{python2_sitelib}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
* Wed Aug 27 2008 Jérôme Soyer <saispo@mandriva.org> 1.2.2-1mdv2009.0
+ Revision: 276469
- New release
* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.1-7mdv2009.0
+ Revision: 259620
- rebuild
* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.1-6mdv2009.0
+ Revision: 247425
- rebuild
* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.1-4mdv2008.1
+ Revision: 171060
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Nov 15 2007 Jérôme Soyer <saispo@mandriva.org> 1.2.1-3mdv2008.1
+ Revision: 108969
- Fix Requires
* Wed Oct 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.2.1-2mdv2008.1
+ Revision: 99746
- Change macros
- Bump release
- Add noarch
- import python-gtkmvc
