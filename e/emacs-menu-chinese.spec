Summary:      Chinese Menu for Emacs
Name:         emacs-menu-chinese
Version:      1.1
Release:      1%{?dist}
License:      GPL
Group:        Applications/Editors/EmacsLisp
BuildArch:    noarch
Source0:      chinese-s-menu.el
Source1:      english-menu.el
Source2:      mule-menu.el
Source3:      chinese-menu-init.el
Source4:      chinese-t-menu.el
Requires:     emacs
BuildRoot:    %{_tmppath}/%{name}-%{version}-root

%description
Chinese menu for Emacs.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/chinese-s-menu.el
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/english-menu.el
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/mule-menu.el
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d/chinese-menu-init.el 
install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/chinese-t-menu.el

%files
%defattr(-,root,root)
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/emacs/site-lisp/site-start.d/*.el

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1-1.ossii
- Add chinese-t-menu.el

* Mon Oct 13 2008 cjacker
- Initial package for Everest Linux
