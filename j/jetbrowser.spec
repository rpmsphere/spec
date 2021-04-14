Name:		jetbrowser
Version:	6.0.425
Release:	5.1
Summary:	An fast, secure and lightweight web browser
License:	CDDL
Group:		Internet
Source0:	JetBrowser-6.0.425.tar.bz2
URL:		http://jetbrowser.codeplex.com/
BuildArch:	noarch

%description
Based on the WebKit engine. It supports tabs, source viewing and inspecting.
It's written in C, HTML, CSS, JavaScript and the user interface in Python.
JetBrowser is a web browser that respects the anonymity of it's users.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
tar xf package.tar -C $RPM_BUILD_ROOT%{_datadir}
cd $RPM_BUILD_ROOT%{_datadir}/webarena
sed -i 's|/opt/|/usr/share/|' %{name}.desktop webarena *.html wa_embed
mv $RPM_BUILD_ROOT%{_datadir}/webarena/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications
rm $RPM_BUILD_ROOT%{_datadir}/webarena/startwarena
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/webarena
./webarena
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/webarena/wa_embed %{buildroot}%{_datadir}/webarena/modules/popmail %{buildroot}%{_datadir}/webarena/modules/pageinfo
sed -i 's|/usr/bin/python |/usr/bin/python2|' %{buildroot}%{_datadir}/webarena/modules/downloader
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/webarena/webarena %{buildroot}%{_datadir}/webarena/modules/yahoostocks %{buildroot}%{_datadir}/webarena/modules/passcardgen

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/webarena
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0.425
- Rebuilt for Fedora
