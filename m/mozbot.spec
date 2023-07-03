Name:           mozbot
Version:        2.6
Release:        2.1
License:        MPL
Source:         https://ftp.mozilla.org/pub/mozilla.org/webtools/%{name}-%{version}.tar.gz
Group:          Applications/Internet
Summary:        Mozilla IRC bot
URL:            https://ftp.mozilla.org/pub/mozilla.org/webtools/
Requires:       perl, wget
BuildArch:      noarch

%description
The IRC bot who hangs out in the #mozilla channel at irc.mozilla.org.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
./%{name}.pl
EOF
cp -a %{name}.pl uuidgen lib config BotModules $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README INSTALL* run-mozbot-*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Jun 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuilt for Fedora

* Wed Sep 30 2009 doiggl@velocitynet.com.au
- packaged mozbot version 2.6 using the buildservice spec file wizard
