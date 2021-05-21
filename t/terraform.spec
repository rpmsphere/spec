Summary: An interactive fractal landscape generator
Name: terraform
Version: 0.9.5
Release: 1
License: GPL
Group: Graphics
Source: terraform-src-%{version}.tgz
URL: http://www.firedrake.org/terraform/
BuildRequires: libglade2-devel
BuildRequires: libgnomeui-devel
#BuildRequires: libgnomeprintui22-devel
BuildRequires: w3m

%description
Terraform is an interactive height field generation and manipulation
program, giving you the ability to generate random terrain and transform it.

%prep
%setup -q -n %{name}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
sed -i 's| $(GNOME_DATADIR)| $(DESTDIR)$(GNOME_DATADIR)|' desktop-links/Makefile
%make_install
mv %{buildroot}/usr/doc %{buildroot}%{_datadir}/doc
install -m644 AUTHORS COPYING ChangeLog README %{buildroot}%{_datadir}/doc/%{name}
install -d %{buildroot}%{_datadir}/applications
sed -e 's| Terrain Editor||' -e '9i Categories=Graphics;' %{buildroot}%{_datadir}/gnome/apps/Graphics/Terraform.desktop > %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -rf %{buildroot}%{_datadir}/gnome/apps %{buildroot}%{_datadir}/gnome/ximian

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/terraform
%{_datadir}/terraform
%{_datadir}/gnome/help/terraform
%{_datadir}/pixmaps/terraform*
%{_datadir}/applications/terraform.desktop
%{_datadir}/doc/%{name}
%{_datadir}/locale/*/LC_MESSAGES/terraform.mo

%changelog
* Tue Mar 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.5
- Rebuilt for Fedora
* Mon Oct 18 1999 Robert Gasch <Robert_Gasch@peoplesoft.com>
- first spec file
