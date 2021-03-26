Name:           nitrotasks 
Version:        1.5.1
Release:        10.1
Summary:        Super awesome task management
License:        BSD
Group:          Applications/Productivity
URL:            http://nitrotasks.com/
Source:         https://github.com/downloads/stayradiated/Nitro/nitrotasks-%{version}.tar.gz
Source1:        %{name}.desktop
Patch1:         nitrotasks-1.5.fc17.1.patch
BuildRequires:       python2-devel
BuildRequires:       python2-distutils-extra
BuildRequires:       intltool
BuildRequires:       desktop-file-utils
BuildArch:  noarch  

%description
Nitro is a super awesome, simple and fast task management application. Nitro packs
a bunch of awesome features such as smart lists, notes, due dates, search and more.
Authors:
Copyright (C) 2012 Caffeinated Code <http://caffeinatedco.de>
Copyright (C) 2012 Jono Cooper
Copyright (C) 2012 George Czabania

%prep
%setup -q
%patch1 -p1

%build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

# This should be solved by the author in the future (data files with executable permissions)
find $RPM_BUILD_ROOT/usr/share/nitrotasks/media -type f | grep -v compile.rb | xargs chmod a-x
rm -Rf $RPM_BUILD_ROOT/usr/share/nitrotasks/media/app/.sass-cache

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_datadir}/help/*/%{name}
%{_datadir}/glib-2.0/schemas
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{python2_sitelib}/*
%doc AUTHORS COPYING 

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora
* Sun Sep 9 2012 Ondrej Hrstka <cybule@gmail.com> - 1.5-1
- Fedora RPM for 1.5 created
* Sun Sep 2 2012 Ondrej Hrstka <cybule@gmail.com> - 1.4.7.2-1
- Fedora RPM for 1.4.7.2 created
* Wed Aug 15 2012 Ondrej Hrstka <cybule@gmail.com> - 1.4.7.1-1
- Fedora RPM for 1.4.7.1 created
* Sun Jul 8 2012 Ondrej Hrstka <cybule@gmail.com> - 1.4.5-1
- Fedora RPM for 1.4.5 created
* Sat Jul 7 2012 Ondrej Hrstka <cybule@gmail.com> - 1.2.5-1
- Package review, first rework of spec file
* Thu May 3 2012 Ondrej Hrstka <cybule@gmail.com> - 1.2.5-1
- Fedora RPM for 1.2.5 created
* Tue May 1 2012 Ondrej Hrstka <cybule@gmail.com> - 1.2.4-1
- Fedora RPM for 1.2.4 created
