%global debug_package %{nil}
%define _name rocketwiki

Name:		rocketwiki-lqfb
Version:	0.4
Release:	1
Summary:	RocketWiki for Liquid Feekback
License:	MIT/X11
Group:		Productivity/Networking
Source0:	http://www.public-software-group.org/pub/projects/rocketwiki/liquid_feedback_edition/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:	ghc-parsec-devel
URL:		http://www.public-software-group.org/webmcp
Provides:	%{_name}

%description
RocketWiki is a small parser written in Haskell which translates a wiki
dialect to HTML. It uses Parsec, a monadic parser combinator library.
The compressed source code of RocketWiki has a size of only 5162 bytes.

%prep
%setup -q -n %{name}-v%{version}

%build
make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/opt/%{_name}
%__install -m755 rocketwiki-lqfb rocketwiki-lqfb-compat %{buildroot}/opt/%{_name}

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE
/opt/%{_name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
