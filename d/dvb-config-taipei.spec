%define __spec_install_post %{nil}

Name:           dvb-config-taipei
Version:        2010
Release:        1
Summary:        Configurations for Linux DVB software
Group:          Applications/Multimedia
License:        GPL
Source0:        %{name}-%{version}.zip
BuildArch:	noarch

%description
Configurations for Linux DVB software.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 644 channels.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer/channels.conf
install -Dm 644 freevo.conf $RPM_BUILD_ROOT%{_sysconfdir}/freevo/freevo.conf
install -Dm 644 local_conf.py $RPM_BUILD_ROOT%{_sysconfdir}/freevo/local_conf.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/mplayer/channels.conf
%{_sysconfdir}/freevo/freevo.conf
%{_sysconfdir}/freevo/local_conf.py

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2010
- Rebuilt for Fedora
