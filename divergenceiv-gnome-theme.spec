%define theme_name A-New-Hope

Summary: %{theme_name} GTK and Metacity theme
Name: divergenceiv-gnome-theme
Version: 0.7.9
Release: 4.1
License: GPL for codes, CC-NC-SA for pixmaps
Group: User Interface/Desktops
Source: %{theme_name}.zip
URL: http://jurialmunkey.deviantart.com/art/Divergence-IV-quot-A-New-Hope-quot-183377193
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: gtk-murrine-engine

%description
Divergence IV is "A New Hope" theme by jurialmunkey.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/%{name} $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
tar zxf %{theme_name}.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/themes
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/A-New-Hope/Configure\ A\ New\ Hope
mv $RPM_BUILD_ROOT%{_datadir}/themes/A-New-Hope/customise.py $RPM_BUILD_ROOT%{_datadir}/%{name}
cp README $RPM_BUILD_ROOT%{_datadir}/%{name}
tar zxf EMERALD/%{theme_name}.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/themes/%{theme_name}
%{_datadir}/%{name}
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Mon May 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.9
- Rebuild for Fedora
