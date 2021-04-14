%undefine _debugsource_packages

Name:               conkywizard
Version:            1.0beta1+r37
Release:            9.1
Summary:            Conky Configuration Wizard
Source:             conkywizard-r37.tar.bz2
Source1:            %{name}.desktop
Patch1:             %{name}-destdir.patch
URL:                http://code.google.com/p/conkywizard/
Group:              System/Monitoring
License:            GNU General Public License version 3 (GPL v3)
BuildRequires:      qt4-devel
Requires:           conky

%description
ConkyWizard is a wizard to set up Conky on Linux.

%prep
%setup -q -n ConkyWizard
%patch1

pushd resources
%__rm translations
%__ln_s ../translations .
popd

%build
qmake-qt4
%__make %{?jobs:-j%{jobs}}

%install
%__make install
%__install -D -m0755 ConkyWizard %{buildroot}%{_bindir}/%{name}
%__install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -D -m0644 resources/graphics/Logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0beta1+r37
- Rebuilt for Fedora
