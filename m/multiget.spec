Name:           multiget
Version:        1.2.1svn
Release:        6.1
Summary:        An easy-to-use GUI file downloader
Group:          Applications/Internet
License:        GPLv2
URL:            https://multiget.sourceforge.net
Source0:        multiget_1.2.1~svn-1.tar.gz
Source1:        multiget.desktop
Source2:        MultiGet.png
BuildRequires:  wxGTK2-devel gcc-c++ libstdc++-devel make
BuildRequires:  intltool libglade2-devel

%description
MultiGet is programmed in C++ and has a GUI based on wxWidgets. It supports HTTP/FTP
protocols which covers the requirements of most users. It supports multi-task
with multi-thread on multi-server. It supports resuming downloads if the Web
server supports it, and if you like, you can reconfig the thread number without
stopping the current task. It's also support SOCKS 4,4a,5 proxy, ftp proxy,
http proxy.

%prep
%setup -qn multiget
chmod 644 icons/*.xpm
chmod 644 newicons/16/*.xpm
chmod 644 newicons/24/*.xpm
chmod 644 newicons/32/*.xpm
chmod 644 newicons/48/*.xpm

%build
%configure 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN/LC_MESSAGES
install -p -m 755 src/multiget $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 po/zh_CN.gmo $RPM_BUILD_ROOT/%{_datadir}/locale/zh_CN/LC_MESSAGES/multiget.mo
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

%files
%doc COPYING
%{_bindir}/multiget
%{_datadir}/applications/multiget.desktop
%{_datadir}/pixmaps/MultiGet.png
%{_datadir}/locale/zh_CN/LC_MESSAGES/multiget.mo

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1svn
- Rebuilt for Fedora
* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.0-5
- include cstdio for sprintf
