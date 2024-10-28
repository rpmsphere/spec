Name:     mikutter
Summary:  The moest twitter client
Version:  0.2.1.1119
Release:  4.1
License:  GPLv3
Group:    Productivity/Networking/Instant Messenger
URL:      https://mikutter.d.hachune.net/
Source0:  https://mikutter.hachune.net/bin/%{name}.%{version}.tar.gz
Source1:  mikutter.desktop
BuildArch:  noarch
Requires: ruby
Requires: ruby-gnome2, rubygem-rcairo
Requires: rubygem-ruby-hmac, rubygem-openssl-nonblock
Requires: libnotify

%description
Simply, powerfully and moefully twitter client.

%description -l ja
みくった〜♪(mikutter)は至高のtwitterクライアントソフトです。

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}/

mkdir $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
exec ruby /usr/share/mikutter/mikutter.rb
EOF

install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -D -m644 core/skin/data/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc LICENSE README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/mikutter.png
%{_datadir}/applications/mikutter.desktop

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3.615
- Rebuilt for Fedora
* Sun Aug 07 2011 kobayashi
- update to 0.0.3.456 unstable
* Mon Jun 20 2011 kobayashi
- update to 0.0.3.9.r414 weekly snapshot
* Mon Jun 13 2011 kobayashi
- update to 0.0.3.8.r405 weekly snapshot
* Thu Jun 02 2011 kobayashi
- update to 0.0.3.6.r375 weekly unstable
* Mon May 16 2011 kobayashi
- update to 0.0.3.4.r322 weekly unstable
* Tue Jan 04 2011 kobayashi
- update to 0.0.2.0 for openSUSE
* Sun Nov 28 2010 tomcat <webmaster2@tomcat.nyanta.jp> 0.0.1.5.r165-1nora103
- update to 0.0.1.5-r165
* Tue Sep 21 2010 tomcat <webmaster2@tomcat.nyanta.jp> 0.0.1.3-0.a3.r120.1nora102
- initial build
