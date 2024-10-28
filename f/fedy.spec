Name:           fedy
Version:        4.0.6
Release:        5.1
Summary:        Software, codec installs and system tweaks
Group:          System/Management
License:        GPL-3.0+
URL:            https://github.com/satya164/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       coreutils
Requires:       curl
Requires:       fedora-release
Requires:       festival
Requires:       grep
Requires:       sed
Requires:       tar
Requires:       unzip
Requires:       util-linux
Requires:       zenity
Obsoletes:      fedorautils

%description
Fedy (previously called as FedoraUtils) lets you install codecs and
additional software, fix problems, tweak and cleanup your system,
view system information and much more with just few clicks.

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING CREDITS README.md
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/polkit-1/actions/*.policy
%{_bindir}/%{name}

%changelog
* Mon Jun 20 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.6
- Rebuilt for Fedora
* Wed Nov 21 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 2.3.0
- various updates
* Thu Jun 28 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 2.1.1
- cleanup, removed repo from postinstall and added as a config file
* Sun Jan 22 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 1.8.1
- policykit support
* Fri Nov 11 2011 Satyajit Sahoo <satyajit.happy@gmail.com> 1.7.6
- added license file
* Tue Oct 25 2011 Satyajit Sahoo <satyajit.happy@gmail.com> 1.7.3
- added postinstall script for adding the repo
* Thu Oct 06 2011 Satyajit Sahoo <satyajit.happy@gmail.com> 1.7.0
- rpm package built with the help of dangermouse
