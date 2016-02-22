%{?scl:%scl_package nodejs-concat-stream}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-concat-stream
Version:    1.4.4
Release:    5%{?dist}
Summary:    Writable stream that concatenates data and calls a callback with the result
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/maxogden/node-concat-stream
Source0:    http://registry.npmjs.org/concat-stream/-/concat-stream-%{version}.tgz

# Use 'stream' module from Node.js core instead of npm(readable-stream).
Patch0:     %{pkg_name}-1.4.4-Use-stream-from-Node.js-core.patch
# npm(typedarray) is taken from https://github.com/inexorabletash/polyfill
# and is for supporting IE-9. But it appears that npm(concat-stream) only
# supports IE>=10 so there doesn't seem to be a compelling reason to use
# typedarray instead of a native `new Uint8Array(len)`.
Patch1:     %{pkg_name}-1.4.4-Remove-dependency-on-typedarray.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(inherits)
BuildRequires:  %{?scl_prefix}npm(tape)
%endif

%description
%{summary}.

%prep
%setup -q -n package
%patch0 -p1
%patch1 -p1
%nodejs_fixdep inherits '~2.0.0'

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/concat-stream
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/concat-stream

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
/usr/bin/tape test/*.js test/server/*.js
%endif

%files
%doc LICENSE readme.md
%{nodejs_sitelib}/concat-stream

%changelog
* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.4.4-5
- Enable SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.4-2
- add missing BR: npm(inherits)

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.4-1
- initial package
