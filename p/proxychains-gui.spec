%undefine _debugsource_packages

Name:       proxychains-gui
Version:        1.4.1
Release:        10.1
License:        GPL-2.0+
Summary:        A Simple GUI Program for the Proxychains Proxifier
URL:            https://sourceforge.net/projects/proxychainsgui
Group:          Productivity/Networking/Web/Proxy
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ qt4-devel
BuildRequires:  desktop-file-utils

%description
proxychains is a tool that forces any TCP connection make by any given
application to follow through proxy like TOR or any other SOCKS4/5 or
HTTP(S) proxy. it supports user/pass auth-type for SOCKS4/5 and basic 
for HTTP. This one is a simple GUI program for it to avoid the CLI work.

%prep
%setup -q

%build
qmake-qt4 PREFIX=/usr
make %{?_smp_mflags}

%install
rm -f -r $RPM_BUILD_ROOT
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/applications/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/

%{__cp} -r src/ProxyChainsGUI $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__cp} -r src/images/icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__cp} -r %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc README
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/

%{_bindir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuilt for Fedora
* Wed Nov 23 2011 i@marguerite.su
- fixed .desktop Categories error, now it is in Utility WebUtility
* Wed Nov 23 2011 i@marguerite.su
- fixed the no binary error. mannual cp everything because the auther
  forgot to write a usable make install in Makefile
* Tue Nov 22 2011 i@marguerite.su
- initial package for 1.4.1
