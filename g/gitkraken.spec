%global privlibs libffmpeg|libnode
%global __requires_exclude ^(%{privlibs})\\.so
%global __provides_exclude_from .*\\.so
#%global debug_package %{nil}

Name: gitkraken
Version: 4.0.2
Release: 1.bin
Summary: Git GUI client
URL: https://www.gitkraken.com/
License: Proprietary
# Release notes: https://support.gitkraken.com/release-notes/current
Source0: https://release.gitkraken.com/linux/gitkraken-amd64.tar.gz#/%{name}-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}.desktop
BuildRequires: desktop-file-utils
BuildRequires: %{_bindir}/convert
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires: libgnome-keyring%{?_isa}
Requires: hicolor-icon-theme
Requires: git%{?_isa}

%description
GitKraken - The legendary Git GUI client for Windows, Mac and Linux.

%prep
%autosetup -n %{name}

%build
# Do nothing...

%install
# Creating general directories...
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}/opt/%{name}/

# Creating ghost file for alternatives system...
touch %{buildroot}%{_bindir}/%{name}

# Installing to working directory from official package...
cp -r %_builddir/%{name} %{buildroot}/opt

# Removing some already installed files...
rm -f %{buildroot}/opt/%{name}/LICENSE*

# Installing icons...
for size in 16 32 48 64 128 256 512; do
    dir="%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps"
    mkdir -p $dir
    convert -resize ${size}x${size} %{SOURCE1} "$dir/%{name}.png"
done

# Marking as executable...
chmod +x %{buildroot}/opt/%{name}/%{name}

# Creating desktop icon...
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} /opt/%{name}/%{name} 10

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} /opt/%{name}/%{name}
fi

%files
%license LICENS*
/opt/%{name}
%ghost %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue Nov 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.2
- Rebuilt for Fedora
* Thu Aug 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.2-1
- Updated to version 4.0.2.
* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.6-1
- Updated to version 3.6.6.
* Fri Jun 29 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.4-1
- Updated to version 3.6.4.
* Mon Jun 11 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-1
- Updated to version 3.6.3.
* Thu May 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.1-1
- Updated to version 3.6.1.
* Tue May 01 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.0-1
- Updated to version 3.6.0.
* Wed Apr 11 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.1-1
- Updated to version 3.5.1.
* Sat Mar 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.4.1-1
- Updated to version 3.4.1.
* Wed Mar 14 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.4.0-1
- Updated to version 3.4.0.
* Thu Feb 01 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.3.4-2
- Updated to version 3.3.4.
* Tue Jan 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.3.3-1
- Updated to version 3.3.3.
* Thu Dec 14 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.3.2-1
- Updated to version 3.3.2.
* Wed Nov 29 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.3.0-1
- Updated to version 3.3.0.
* Sun Nov 19 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.2-1
- Updated to version 3.2.2.
* Wed Nov 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.1-1
- Initial SPEC release.
