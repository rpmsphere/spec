#
# spec file for package moblin-panel-datetime (version 0.2.5)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           moblin-panel-datetime
Version:        0.2.7
Release:        1.8
License:        GPL v2 or later
Summary:        Date/Time panel
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.16.1
BuildRequires:  intltool >= 0.35.5
BuildRequires:  jana-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgweather-devel
BuildRequires:  libnotify-devel
BuildRequires:  moblin-panel-myzone-devel
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  mutter-moblin-devel
BuildRequires:  libmx-devel
BuildRequires:  pkgconfig(penge)
##%gconf_schemas_prereq

%description
Date and Time panel which features world clock and alarm support

%prep
%setup -q

%build
%configure
make

%install
%makeinstall
##%find_gconf_schemas
%find_lang %{name}

%clean
rm -rf %{buildroot}

%pre -f %{name}.schemas_pre

%preun -f %{name}.schemas_preun

%posttrans -f %{name}.schemas_posttrans

%files -f %{name}.schemas_list -f %{name}.lang
%defattr(-, root, root)
%{_libexecdir}/moblin-panel-datetime
%{_datadir}/dbus-1/services/org.moblin.UX.Shell.Panels.datetime.service
%{_datadir}/moblin-panel-datetime
%{_datadir}/mutter-moblin/panels/moblin-panel-datetime.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Mon Jul 19 2010 awafaa@opensuse.org
- Update to version 0.2.7
* Mon Jun 28 2010 awafaa@opensuse.org
- Clean up & re-write spec file to thanks to DimStar
* Tue Jun 15 2010 dimstar@opensuse.org
- BuildRequire pkgconfig(gconf-2.0) instead of GConf2-devel.
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import into openSUSE version 0.2.5
