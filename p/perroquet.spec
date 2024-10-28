%undefine _debugsource_packages
Summary:        A listening comprehension tutor
Name:           perroquet
Version:        1.1.1
Release:        9.1
Source0:        https://launchpad.net/perroquet/1.1/1.1.1/+download/%{name}-%{version}.tar.gz
License:        GPLv3
Group:          Education
URL:            https://perroquet.b219.org
BuildRequires:  python2-devel
BuildRequires:  intltool
BuildRequires:  python2-setuptools
BuildRequires:  desktop-file-utils
Requires:       gtk2
Requires:       gstreamer-plugins-good
Requires:       python2-gstreamer
Requires:       pygtk2
BuildArch:      noarch

%description
Perroquet is a educational program to improve playfully your listening in a
foreign language.

The principle of Perroquet is to use a video or audio file and the associated
subtitles to make you listen and understand the dialogue or lyrics. After
having identified the files to use, Perroquet will read a piece of video then
pause. It will show you the number of words to find and you will have to type
them to continue. You can listen a sequence as many times as necessary.
If you do not understand, Perroquet offers several means to help you.

%prep
%setup -q

%build
python2 setup.py build 

%install
%__rm -rf $RPM_BUILD_ROOT
python2 setup.py \
        --without-icon-cache \
        --without-mime-database \
        --without-desktop-database \
        install --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

desktop-file-install \
        --remove-key=Encoding \
        --remove-category=Application \
        --add-category=Languages \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %name

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files -f %{name}.lang
%doc README AUTHORS ChangeLog NEWS MAINTAINERS
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/%{name}.xml
%{_sysconfdir}/%{name}

%changelog
* Tue May 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Sat Jan 16 2010 Jérôme Brenier <incubusss@mandriva.org> 1.0.1-2mdv2010.1
+ Revision: 492482
- use Education for the Group tag
- fix desktop file (and BR desktop-file-utils)
* Sat Jan 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 491950
- import perroquet
