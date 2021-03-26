Name:           rpmdiagram
Version:        1.0
Release:        2.1
Summary:        Draws diagrams of RPM dependencies
Group:          Applications/System
License:        GPLv2
URL:            http://software.amiga-hardware.com
Source0:        http://software.amiga-hardware.com/software/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(GraphViz)
BuildArch:      noarch

%description
Draws diagrams of installed RPM dependencies using GraphViz and outputs the
diagram into an image file such as PNG or JPG.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir} %{buildroot}%{_datadir}/%{name}
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0644 %{name}.cfg %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%doc examples README COPYING

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
* Tue May 06 2009 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-1%{?dist}
- Initial release
