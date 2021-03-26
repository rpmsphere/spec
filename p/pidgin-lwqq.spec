%global debug_package %{nil}

Name:       pidgin-lwqq
Version:	2.0a.fix
Release:	7.4
License:	SuSE-Permissive
Summary:	A pidgin plugin based on lwqq
URL:	https://github.com/xiehuc/pidgin-lwqq
Group:	Productivity/Networking/Instant Messenger
Source:	%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libcurl-devel
BuildRequires:	libev-devel
BuildRequires:	libpurple-devel
BuildRequires:	sqlite-devel
BuildRequires:	pidgin
#BuildRequires:  empathy

%description
A pidgin QQ plugin based on lwqq, an excellent safe useful library
for webqq protocol.

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir} ..
make %{?_smp_mflags}

%install
cd build
%make_install



%files
%doc AUTHORS ChangeLog README.md KnownIssue.md
%{_datadir}/pixmaps/pidgin/emotes/webqq
%{_datadir}/pixmaps/pidgin/emotes/webqq_static
%{_datadir}/pixmaps/pidgin/protocols/*/*
%{_datadir}/icons/hicolor/*/apps/webqq.*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_libdir}/purple-2/libwebqq.so

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0a.fix
- Rebuild for Fedora
* Thu Aug  1 2013 i@marguerite.su
- update 2.0a.fix
  * use libcurl internal cookie engine
  * add syslog
* Thu Aug  1 2013 i@marguerite.su
- update 2.0a
  * windows support
  * change libwebqq hash again
  * add with libev optional
* Thu Jul 18 2013 hillwood@linuxfans.org
- update to 1.0f
  * fix issue #335
  * clean compile warnning
  * use long long type in hashP
  * change curl find path
  * add fflush to cli
- split package
* Sun May 12 2013 xiehuc@gmail.com
- update version 1.0e
  * full support discu
  * support passerby
  * add relink option
* Fri Apr 19 2013 i@marguerite.su
- emergency fix:  add hashO.
* Wed Apr 17 2013 i@marguerite.su
- emergency add get friend hash. (protocol change)
* Sat Apr 13 2013 i@marguerite.su
- update version 1.0d.
  * ssl support
  * group online history
  * add upload offline file runtime option
  * finish block chat menu
  * other bugfixes
* Thu Feb 28 2013 i@marguerite.su
- update version 1.0c. Changes since 20121224:
  * new feature: less lost connection
  * new feature: add friend & group
  * new feature: change self business card for group.
  * new feature: support long nick
  * new feature: support change group/discu markname
  * new feature: support chat topic
  * new feature: support download chat log
  * enhancement: slow down cpu rate by add libev time interval
  * enhancement: add timeout retry 3 times.
  * enhancement: file transport enhanced
* Mon Dec 24 2012 i@marguerite.su
- update version 20121224
  * new feature: add fast index to speed up qqnumber/uin lookup.
  * new feature: support local qqnumber cache.
  * new feature: support send/recv offline file.
  * new feature: support recv file trans.
  * new feature: support block group message.
  * new feature: support font style.
  * bug&compile fixes.
* Sun Sep  2 2012 i@marguerite.su
- initial version 20120826
  * new feature: not official support for offline file.
