Summary:      Locale support for Emacs
Name:         emacs-locale
Version:      24.3
Release:      1
License:      GPL
Group:        Applications/Editors/EmacsLisp
BuildArch:    noarch
Source0:      %{name}-%{version}.tar.gz
Requires:     emacs

%description
Currently with translations for simplified and traditional chinese.

%prep
%setup -q -n %{name}

%build

%install
%make_install

%files
%{_datadir}/doc/emacs-locale
%{_datadir}/emacs/site-lisp/locale
%{_datadir}/emacs/site-lisp/site-start.d/locale-init.el

%changelog
* Tue Apr 08 2014 Wei-Lun Chao <bluebat@member.fsf.org> 24.3-1
- Initial package
