Name:           ponysay
Version:        3.0.3
Release:        1
Summary:        Cowsay reimplemention for ponies
License:        GPL-3.0+
Group:          Amusements/Toys/Other
URL:            https://github.com/erkin/ponysay
Source:         https://github.com/erkin/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  texinfo
BuildArch:      noarch

%description
ponysay as an awesome terminal application to display ponies speaking
messages in your terminal.
It has many features; you can use its info manual to explore them.

%prep
%setup -q

%build
# Nothing to build.

%install
python3 setup.py \
  --dest-dir=%{buildroot} \
  --prefix=%{_prefix} \
  --freedom=partial \
  --with-everything \
  --with-pdf=%{_docdir}/%{name}/ \
  install
rm -r %{buildroot}%{_infodir}/dir \
  %{buildroot}%{_datadir}/licenses/ \
  %{buildroot}%{_datadir}/doc/%{name}

%files
%doc CHANGELOG CONTRIBUTING COPYING CREDITS LICENSE README.md %{name}.pdf
%{_bindir}/pony*
%{_datadir}/%{name}
%{_infodir}/*
%{_mandir}/*/*
%{_datadir}/bash-completion/*
%{_datadir}/zsh/*
%{_datadir}/fish/*

%changelog
* Tue Nov 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.3
- Rebuilt for Fedora
* Sun Mar 12 2017 sor.alexei@meowr.ru
- Explicitly package %%{_docdir}/%%{name}/.
* Sat Sep  6 2014 sor.alexei@meowr.ru
- Update to 3.0.2
  * New ponies: auntorange, grace
  * Pony symlink added:
  - cookiecrumbles → raritysmom (official name)
  - hondoflanks → raritysdad (official name)
  * Special pony cases:
  - orange was renamed to uncleorange to not conflict with
    auntorange.
- Remove info-direntry.patch: fixed upstream.
* Sat Apr 26 2014 andreas.stieger@gmx.de
- spec cleanup.
- Add source URLs.
* Sun Apr  6 2014 sor.alexei@meowr.ru
- Initial package.
