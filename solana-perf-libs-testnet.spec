%global solana_suffix testnet

Name:       solana-perf-libs-%{solana_suffix}
Version:    0.19.3
Release:    1%{?dist}
Summary:    C and CUDA libraries to enhance Solana (no CUDA, only SIMD)

License:    Apache-2.0
URL:        https://github.com/solana-labs/solana-perf-libs/
Source0:    https://github.com/solana-labs/solana-perf-libs/archive/v%{version}/solana-perf-libs-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ispc


%description
C and CUDA libraries to enhance Solana (no CUDA, only SIMD).


%prep
%autosetup -b0 -n solana-perf-libs-%{version}


%build
cd src/poh-simd
%make_build ISPC_FLAGS="-g -O2 --pic -I."


%install
mkdir -p %{buildroot}/opt/solana/%{solana_suffix}/bin/perf-libs
cp -p \
        src/poh-simd/libs/libpoh-simd.so \
        %{buildroot}/opt/solana/%{solana_suffix}/bin/perf-libs/


%files
/opt/solana/%{solana_suffix}/bin/perf-libs/libpoh-simd.so


%changelog
* Sat Feb 13 2021 Ivan Mironov <mironov.ivan@gmail.com> - 0.19.3-1
- Initial packaging
