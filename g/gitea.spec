%undefine _debugsource_packages
%global _default_patch_fuzz 2

Name:		gitea
Version:	1.20.1
Release:	1
Summary:	Git with a cup of tea, painless self-hosted git service
License:	MIT
Group:		Development/Other
URL:		https://gitea.io/
Source0:	https://github.com/go-gitea/gitea/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:	gitea.service
Source11:	gitea.service.d.conf
Source12:	app-gitea.ini
Patch0:		make-version.patch
Requires:	git-core
BuildRequires:	golang make
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  npm

%description
The goal of this project is to make the easiest, fastest, and most painless way
of setting up a self-hosted Git service. It is similar to GitHub, Bitbucket,
and Gitlab. Gitea is a fork of Gogs.

%prep
%autosetup -p1

%build
export GOPATH="`pwd`/.godeps"
export LDFLAGS='-X "main.MakeVersion=GNU Make 4.3" -X "main.Version=%{version}" -X "main.Tags=bindata sqlite sqlite_unlock_notify pam"'
TAGS="bindata sqlite sqlite_unlock_notify pam" make VERSION=%{version} generate all

%install
mkdir -p %buildroot/srv/%{name}
mkdir -p %buildroot%{_localstatedir}/log/%{name}
install -Dm 0755 %name %buildroot%_bindir/%{name}
install -Dm 0640 %SOURCE10 %buildroot%_unitdir/%{name}.service
mkdir -p %buildroot%_sysconfdir/systemd/system/gitea.service.d
install -Dm 0640 %SOURCE11 %buildroot%_sysconfdir/systemd/system/gitea.service.d/port.conf
install -Dm 0660 %SOURCE12 %buildroot%_sysconfdir/%{name}/app.ini

# install docs
mkdir -p %buildroot%_docdir/%name
install -Dm 0644 "custom/conf/app.example.ini" \
	%buildroot%_docdir/%name/default-app.ini

%pre
useradd gitea -d /srv/gitea -s /sbin/nologin

%postun
userdel gitea

%files
%_bindir/%name
%dir %attr(0700,%name,%name) /srv/%name
%dir %attr(0700,%name,%name) %{_localstatedir}/log/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0660,root,%name) %_sysconfdir/%name/app.ini
%config(noreplace) %attr(0660,root,%name) %_sysconfdir/systemd/system/gitea.service.d/port.conf
%_unitdir/%name.service
%_docdir/%name/default-app.ini
%doc *.md

%changelog
* Sun Jul 23 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.20.1
- Rebuilt for Fedora
