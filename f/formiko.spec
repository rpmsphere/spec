Name: formiko
Summary: reStructuredText and MarkDown editor and live previewer
Version: 1.3.0
Release: 4.1
Group: editors
License: BSD
URL: https://github.com/ondratu/formiko
Source0: https://github.com/ondratu/formiko/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel

%description
Features:
 * GtkSourceView based editor with syntax highlighting
 * possible use Vim editor
 * vertical or horizontal window splitting
 * preview mode
 * periodic save file
 * json and html preview

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-vim
%{python3_sitelib}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-vim.desktop
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Mon Oct 29 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
