Name:           moblin-sound-theme
Version:        0.3
Release:        3.1
Summary:        Moblin sound theme
Group:          System/GUI/Other
Source0:        moblin-sound-theme-%{version}.tar.bz2
# For details on the licenses used, see README
License:        GPLv2+
URL:            http://www.moblin.org
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  intltool

%description
The sound theme used in the Moblin UX.

%prep
%setup -q

%build
%configure

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_datadir}/sounds/moblin

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Tue Mar 23 2010 awafaa@opensuse.org
- Fix %%install section to comply with Factory requirements
* Mon Mar 22 2010 awafaa@opensuse.org
- Update Group to System/GUI/Other
- Expand description
* Wed Aug 19 2009 abockover@novell.com
- created package
* Wed May 13 2009 damien.lespiau@intel.com
- First sound theme package
