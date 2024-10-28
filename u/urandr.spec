%define __python /usr/bin/python2
%undefine _debugsource_packages
Name:          urandr
Version:       0.1
Release:       7.1
Summary:       A GUI to RandR 1.2
Group:         Graphical Desktop/Applications/Configuration
URL:           https://albertomilone.com/urandr.html
Source:        https://albertomilone.com/ubuntu/urandr/urandr-%{version}.tar.gz
License:       GPL
BuildRequires:  python2
BuildArch: noarch
Requires: pygtk2-libglade

%description
Urandr is a GUI to RandR 1.2 written in PyGTK. It covers RandR 1.2 basic
functionalities and aims to make multihead configuration as easy as possible
for unexperienced users.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitearch}
%find_lang %{name}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
./randrgtk.py \$USER \$HOME \$UID \$1
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python2_sitearch}/URandR/*
%{python2_sitearch}/urandr-*-info
%{_datadir}/%{name}

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Mon Jan 26 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1-2mamba
- fixed License field
* Sun Jan 18 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1-1mamba
- package created by autospec
