Name: conan
Version: 1.21.0
Release: 1%{?dist}

Summary: The open-source C/C++ package manager
License: MIT
URL: https://github.com/conan-io/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel

BuildRequires: python3dist(requests)
BuildRequires: python3dist(six)
BuildRequires: python3dist(colorama)
#BuildRequires: python3dist(patch)
BuildRequires: python3dist(fasteners)
BuildRequires: python3dist(semver)
BuildRequires: python3dist(distro)
BuildRequires: python3dist(pylint)
BuildRequires: python3dist(future)
BuildRequires: python3dist(pygments)
BuildRequires: python3dist(astroid)
BuildRequires: python3dist(pluginbase)
BuildRequires: python3dist(bottle)

BuildRequires: PyYAML
BuildRequires: python3-PyYAML
BuildRequires: python3-jwt

Requires: python3-PyYAML
%{?python_provide:%python_provide python3-%{name}}

%description
Conan is a package manager for C and C++ developers.

It is fully decentralized. Users can host their packages in their
servers, privately. Integrates with Artifactory and Bintray.

Portable. Works across all platforms, including Linux, OSX, Windows
(with native and first-class support, WSL, MinGW), Solaris, FreeBSD,
embedded and cross-compiling, docker, WSL.

Manage binaries. It can create, upload and download binaries for any
configuration and platform, even cross-compiling, saving lots of
time in development and continuous integration. The binary
compatibility can be configured and customized. Manage all your
artifacts in the same way on all platforms.

Integrates with any build system, including any proprietary and
custom one. Provides tested support for major build systems (CMake,
MSBuild, Makefiles, Meson, etc).

Extensible: Its python based recipes, together with extensions points
allows for great power and flexibility.

Large and active community, especially in Github and Slack. This
community also creates and maintains packages in Conan-center and
Bincrafters repositories in Bintray.

Stable. Used in production by many companies, since 1.0 there is a
commitment not to break package recipes and documented behavior.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE.md
%doc README.rst
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.egg-info

%changelog
* Wed Dec 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.21.0-1
- Updated to version 1.21.0.
