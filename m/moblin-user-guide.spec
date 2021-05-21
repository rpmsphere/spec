#
# spec file for package moblin-user-guide (Version 2.1.10)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:		moblin-user-guide
Version:	2.1.10
Release:	2.1
Summary:	User Guide for Moblin
URL:		http://moblin.org/

Group:		Documentation/Other
License:	Open Publication
Source0:	moblin-user-guide-%{version}.tar.bz2
Source1:        moblin-logo-icon.png

BuildArch:	noarch
BuildRequires:	desktop-file-utils
##BuildRequires:	fdupes
BuildRequires:  hicolor-icon-theme
Patch0:         meego.patch
Patch1:         moblin-user-guide-suse-category.patch

%description 
User Guide for Moblin

%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
# One day maybe we'll use Publican here.


%install
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/gnome/help/moblin-user-guide
pushd moblin-user-guide
find  -type f -exec install -m 644 -D {} $RPM_BUILD_ROOT%{_datadir}/gnome/help/moblin-user-guide/{} \;
popd
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/omf/moblin-user-guide
install -m 644 moblin-user-guide-*omf $RPM_BUILD_ROOT%{_datadir}/omf/moblin-user-guide
install -m 644 -D about-moblin.desktop $RPM_BUILD_ROOT%{_datadir}/applications/about-moblin.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/moblin-logo-icon.png

##%fdupes -s %{buildroot}/%_datadir
%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ -x /usr/bin/scrollkeeper-update ]; then scrollkeeper-update -q -o %{_datadir}/omf/%{name}:%{_datadir}/omf/moblin-user-guide ; fi
if [ -x /usr/bin/update-desktop-database ]; then update-desktop-database &> /dev/null; fi

%postun
if [ -x /usr/bin/scrollkeeper-update ]; then scrollkeeper-update -q; fi
if [ -x /usr/bin/update-desktop-database ]; then update-desktop-database &> /dev/null; fi


%files
%defattr(-,root,root,-)
%{_datadir}/gnome/help/moblin-user-guide/
%{_datadir}/applications/about-moblin.desktop
%{_datadir}/omf/moblin-user-guide/
%{_datadir}/icons/hicolor/48x48/apps/moblin-logo-icon.png


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Jul 13 2010 glin@novell.com
- Add moblin-logo-icon.png as the icon of moblin-user-guide
- Assign Category for about-moblin.desktop
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import into openSUSE version 2.1.10
