Name:           paper-gnome-theme
Version:        2.1.0
Release:        3.1
Summary:        The 'Paper' GNOME theme
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://snwh.org/paper
Source:         https://github.com/snwh/paper-gtk-theme/archive/v%{version}.tar.gz#/paper-gtk-theme-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildArch:      noarch
Provides:       paper-gtk-theme
Requires:       paper-icon-theme

%description
Paper is a modern desktop theme suite. Its design is mostly flat
with a minimal use of shadows for depth.

%prep
%setup -q -n paper-gtk-theme-%{version}
chmod a-x README.md Paper/gtk-2.0/gtkrc

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%doc AUTHORS LICENSE README.md
%{_datadir}/themes/Paper/

%changelog
* Wed Jul 25 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuild for Fedora
* Wed Nov 23 2016 sor.alexei@meowr.ru
- Divide paper-gtk-theme to metatheme-paper-common, and
  gtk{2,3}-metatheme-paper.
- Don't require gtk2-engines, instead recommend
  gtk2-theming-engine-adwaita.
- Spec cleanup.
* Sun Jun  5 2016 mailaender@opensuse.org
- initial packaging of version 2.1.0
