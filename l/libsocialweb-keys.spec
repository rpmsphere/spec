Name: libsocialweb-keys
Summary: API keys for libsocialweb
Group: System Environment/Desktop
Version: 1
License: LGPL 2.1
URL: https://www.moblin.org
Release: 1
Source0: lastfm
Source1: twitter
Source2: digg
Source3: flickr
Source4: myspace
Source5: facebook
BuildArch: noarch

%description
Last.fm and Twitter API keys for libsocialweb.

%prep
%setup -T -c -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

%define keydir %{_datadir}/libsocialweb/keys
%{__mkdir_p} %{buildroot}/%{keydir}
cp %{SOURCE0} %{buildroot}/%{keydir}
cp %{SOURCE1} %{buildroot}/%{keydir}
cp %{SOURCE2} %{buildroot}/%{keydir}
cp %{SOURCE3} %{buildroot}/%{keydir}
cp %{SOURCE4} %{buildroot}/%{keydir}
cp %{SOURCE5} %{buildroot}/%{keydir}

%files
%{keydir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Mon Sep 20 2010 awafaa@opensuse.org
- Fix MySpace key - use new key
* Fri Sep 17 2010 awafaa@opensuse.org
- Fix Flickr key - use new key
* Wed Sep 15 2010 awafaa@opensuse.org
- Fix Facebook key - use upstream MeeGo's key
* Thu Jul 22 2010 awafaa@opensuse.org
- Fix key layouts - split keys onto seperate lines
* Wed Jul  7 2010 awafaa@opensuse.org
- Add digg, flickr, myspace & facebook keys
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import for openSUSE version 1
