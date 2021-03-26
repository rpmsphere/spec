%global debug_package %{nil}
Name:           httpripper
Version:        1.1.1
Release:        5.1
Summary:        HTTP Ripper is a tool to rip content out of the web.
Group:          Networking/WWW
License:        GPLv3
URL:            http://29a.ch/httpripper/
Source0:        http://29a.ch/httpripper/%{name}-%{version}.tar.gz
BuildRequires:  python2-devel desktop-file-utils
BuildArch:      noarch
Requires: 	pygtk2

%description
HTTP Ripper is a generic ripper for the web

Usage
=====
Start HTTPRipper. It will display the hostname/port it's running on.
Configure your browser to use it as proxy. Hit the record button ;)
For information on how to use httpripper please visit the website.
http://29a.ch/httpripper/

Examples
  * Download movies from YouTube and other Video sites
  * Download music of you favorite bands MySpace site
 Features
  * Free Software (GPL 3)
  * Runs on GNU/Linux and Windows
  * Nearly undetectable / blockable by servers
  * Built with python and pygtk

%prep
%setup -q 

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install -O1 --skip-build --root=%{buildroot}

desktop-file-install --vendor="" \
     --remove-category="Application" \
     --add-category="Network;FileTransfer" \
     --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/pixmaps/%{name}.png
%{python2_sitelib}/*

%changelog
* Wed Feb 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1-2
- Rebuild for Fedora
* Sat Sep 11 2010 Texstar <texstar at gmail.com> 1.1.1-1pclos2009
- Update
* Sun Jun 07 2009 slick50 <lxgator@gmail.com> 1.0.0-1pclos2009
- initial build
